from abc import ABC, abstractmethod
from typing import Any, Dict, List

class BaseScraper(ABC):
    """Base interface for all data scrapers"""
    
    @abstractmethod
    async def fetch_data(self) -> List[Dict[str, Any]]:
        """Fetch data from source"""
        pass
    
    @abstractmethod
    async def transform_data(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Transform data into standardized format"""
        pass
