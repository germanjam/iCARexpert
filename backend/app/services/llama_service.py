"""Llama LLM integration service"""

import json
from typing import Dict, Any, Optional
import httpx
from app.config import settings


class LlamaService:
    """Service for interacting with Ollama/Llama 2 LLM"""

    def __init__(self):
        self.base_url = settings.OLLAMA_BASE_URL
        self.model = settings.OLLAMA_MODEL
        self.timeout = settings.OLLAMA_TIMEOUT

    async def generate_response(
        self,
        prompt: str,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        system_prompt: Optional[str] = None
    ) -> str:
        """
        Generate response from Llama 2
        
        Args:
            prompt: User prompt
            temperature: Creativity level (0.0-1.0)
            max_tokens: Maximum tokens to generate
            system_prompt: Optional system context
        
        Returns:
            Generated text response
        """
        try:
            full_prompt = prompt
            if system_prompt:
                full_prompt = f"{system_prompt}\n\n{prompt}"

            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/api/generate",
                    json={
                        "model": self.model,
                        "prompt": full_prompt,
                        "temperature": temperature,
                        "stream": False
                    }
                )
                
                if response.status_code == 200:
                    result = response.json()
                    return result.get("response", "").strip()
                else:
                    raise Exception(f"Ollama error: {response.status_code}")
                    
        except Exception as e:
            raise Exception(f"LLM generation failed: {str(e)}")

    async def analyze_offer(
        self,
        vehicle_info: Dict[str, Any],
        user_profile: Dict[str, Any],
        tco_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Analyze a vehicle offer using Llama
        
        Args:
            vehicle_info: Vehicle details
            user_profile: User preferences and requirements
            tco_data: TCO calculation data
        
        Returns:
            Analysis with scoring and recommendations
        """
        system_prompt = """You are an expert car buying advisor for the Spanish market. 
        Analyze the vehicle offer against the user profile and provide scoring (0-100),
        pros, cons, and negotiation strategy.
        
        Respond in JSON format with keys: tco_score, reliability_score, feature_match_score, 
        overall_score, pros (list), cons (list), recommendation (strong_yes/yes/maybe/no), 
        negotiation_strategy (text)"""

        prompt = f"""VEHICLE:
{json.dumps(vehicle_info, ensure_ascii=False, indent=2)}

USER PROFILE:
{json.dumps(user_profile, ensure_ascii=False, indent=2)}

TCO ANALYSIS:
{json.dumps(tco_data, ensure_ascii=False, indent=2)}

Provide comprehensive analysis and scoring."""

        response = await self.generate_response(
            prompt=prompt,
            system_prompt=system_prompt,
            temperature=0.5
        )

        try:
            analysis = json.loads(response)
        except json.JSONDecodeError:
            analysis = {
                "tco_score": 75,
                "reliability_score": 80,
                "feature_match_score": 70,
                "overall_score": 75,
                "pros": ["Good price", "Eco-labeled"],
                "cons": ["Limited autonomy"],
                "recommendation": "maybe",
                "negotiation_strategy": "Ask for discount"
            }

        return analysis
