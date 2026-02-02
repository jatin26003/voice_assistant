# News Module (Stubbed - no API key required)
import random
from datetime import datetime

class NewsService:
    def __init__(self):
        self.stub_headlines = [
            "Local Team Wins Championship Game",
            "New Technology Breakthrough Announced",
            "Weather Patterns Shifting Globally",
            "Economic Markets Show Positive Growth",
            "Scientific Discovery Changes Understanding",
            "Community Event Draws Large Crowd",
            "New Policy Implementation Begins",
            "Health Study Reveals Surprising Results",
            "Environmental Initiative Launched",
            "Cultural Festival Celebrates Heritage"
        ]
        
        self.categories = ['technology', 'science', 'health', 'business', 'entertainment', 'sports']
    
    def get_headlines(self, category=None):
        """Get news headlines (stubbed)"""
        if category and category.lower() in self.categories:
            # Filter headlines by category (simplified)
            filtered = [h for h in self.stub_headlines if category.lower() in h.lower()]
            headlines = filtered if filtered else random.sample(self.stub_headlines, 3)
        else:
            headlines = random.sample(self.stub_headlines, 5)
        
        result = f"Latest headlines ({datetime.now().strftime('%H:%M')}):\n"
        for i, headline in enumerate(headlines, 1):
            result += f"{i}. {headline}\n"
        
        return result
    
    def get_news_summary(self):
        """Get news summary (stubbed)"""
        summary = random.choice([
            "Markets are up today with technology stocks leading gains.",
            "Breaking: Major scientific breakthrough announced in renewable energy.",
            "Weather officials predict mild conditions for the coming week.",
            "Local elections results show surprising outcomes in several districts.",
            "Health officials report positive trends in recent wellness studies."
        ])
        
        return f"News Summary: {summary}"
    
    def search_news(self, query):
        """Search news (stubbed)"""
        # Simple keyword matching in stub headlines
        matching = [h for h in self.stub_headlines if query.lower() in h.lower()]
        
        if not matching:
            return f"No news found for '{query}'"
        
        result = f"News results for '{query}':\n"
        for headline in matching[:3]:
            result += f"- {headline}\n"
        
        return result
