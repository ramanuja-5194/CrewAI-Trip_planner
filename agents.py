from crewai import Agent
from textwrap import dedent
from langchain_google_genai import ChatGoogleGenerativeAI
from tools.search_tools import SearchTools # Import the direct tool
from tools.calculator_tools import CalculatorTools # Import the direct tool


"""
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee
    you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal.
- Define which experts the captain needs to communicate with and delegate tasks to.
    Build a top down structure of the crew.

Goal:
- Create a 7-day travel itinerary with detailed per-day plans,
    including budget, packing suggestions, and safety tips.

Captain/Manager/Boss:
- Expert Travel Agent

Employees/Experts to hire:
- City Selection Expert
- Local Tour Guide


Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume
"""

# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class TravelAgents:
    def __init__(self):
        self.GEMINI25FLASH = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.7)
        # No need to instantiate SearchTools or CalculatorTools here if importing directly
        # self.search_tools_instance = SearchTools()
        # self.calculator_tools_instance = CalculatorTools()

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent("""Expert in travel planning and logistics.
                                I have decade of experience making travel itineraries."""),
            goal=dedent("""Create a 7-day travel itinerary with detailed per-day plans,
                            include budget, packing suggestions, and safety tips."""),
            tools=[
                SearchTools, # Directly use the imported tool
                CalculatorTools        # Directly use the imported tool
            ],
            verbose=True,
            llm=self.GEMINI25FLASH,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""Expert at analyzing travel data to pick ideal destinations."""),
            goal=dedent(f"""Select the best cities based on weather, season, prices, and traveler interests"""),
            tools=[SearchTools], # Directly use the imported tool
            verbose=True,
            llm=self.GEMINI25FLASH,
        )
    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""Knowledgeable local guide with extensive information
                                about the city, it's attractions and customs
                                """),
            goal=dedent(f"""Provide the BEST insights about the selected city"""),
            tools=[SearchTools], # Directly use the imported tool
            verbose=True,
            llm=self.GEMINI25FLASH,
        )