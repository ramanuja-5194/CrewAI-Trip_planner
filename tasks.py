# To know more about the Task class, visit: https://docs.crewai.com/concepts/tasks
from crewai import Task
from textwrap import dedent

"""
Creating Tasks Cheat Sheet:
- Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal:
- Develop a detailed itinerary, including city selection, attractions, and practical travel advice.

Key Steps for Task Creation:
1. Identify the Desired Outcome: Define what success looks like for your project.
   - A detailed 7 day travel itenerary.

2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
   - Itenerary Planning: develop a detailed plan for each day of the trip.
   - City Selection: Analayze and pick the best cities to visit.
   - Local Tour Guide: Find a local expert to provide insights and recommendations.

3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.

4. Task Description Template:
 - Use this template as a guide to define each task in your CrewAI application.
 - This template helps ensure that each task is clearly defined, actionable, and aligned with the specific goals of your project.

 Template:
 ---------
 def [task_name](self, agent, [parameters]):
     return Task(description=dedent(f'''
     **Task**: [Provide a concise name or summary of the task.]
     **Description**: [Detailed description of what the agent is expected to do, including actionable steps and expected outcomes. This should be clear and direct, outlining the specific actions required to complete the task.]

     **Parameters**:
     - [Parameter 1]: [Description]
     - [Parameter 2]: [Description]
     ... [Add more parameters as needed.]

     **Note**: [Optional section for incentives or encouragement for high-quality work. This can include tips, additional context, or motivations to encourage agents to deliver their best work.]

     '''), agent=agent)

"""

class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def plan_itinerary(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
                **Task**: Plan a 7-Day Travel Itinerary
                **Description**: Expand the city guide into a full 7-day travel itinerary with detailed
                per-day plans, including weather forecasts, places to eat, packing suggestions,
                and a budget breakdown. You MUST suggest actual places to visit, actual hotels to stay,
                and actual restaurants to go to. This itinerary should cover all aspects of the trip,
                from arrival to departure, integrating the city guide information with practical travel logistics.

                **Parameters**:
                - City: {city}
                - Trip Date: {travel_dates}
                - Traveler Interests: {interests}

                **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            expected_output=dedent(
                """
                A complete 7-day travel itinerary in a single, well-formatted markdown file.
                The itinerary must include:
                - A detailed plan for each of the 7 days, with specific times, locations, and activity descriptions.
                - Suggestions for at least 3 real hotels with estimated prices.
                - Recommendations for breakfast, lunch, and dinner for each day.
                - A packing list tailored to the destination's weather.
                - A section with a daily and total budget breakdown.
                - Safety tips relevant to the chosen city.
                """
            ),
        )

    def identify_city(self, agent, origin, cities, interests, travel_dates):
        return Task(
            description=dedent(
                f"""
                **Task**:   Identify the Best City for the Trip
                **Description**: Analyze and select the best city for the trip based on specific
                    criteria such as weather patterns, seasonal events, and travel costs.
                    This task involves comparing multiple cities, considering factors like current weather
                    conditions, upcoming cultural or seasonal events, and overall travel expenses.
                    Your final answer must be a detailed report on the chosen city,
                    including actual flight costs, weather forecast, and attractions.


                **Parameters**:
                - Origin: {origin}
                - Cities: {cities}
                - Interests: {interests}
                - Travel Date: {travel_dates}

                **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            expected_output=dedent(
                """
                A detailed report on the single best city to visit.
                The report must include:
                - The name of the chosen city.
                - A paragraph explaining why it's the best choice.
                - A 7-day weather forecast for the travel dates.
                - An estimated round-trip flight cost from the origin.
                - A list of 5 key attractions that match the traveler's interests.
                """
            ),
        )

    def gather_city_info(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
                    **Task**:   Gather In-depth City Guide Information
                    **Description**: Compile an in-depth guide for the selected city, gathering information about
                        key attractions, local customs, special events, and daily activity recommendations.
                        This guide should provide a thorough overview of what the city has to offer, including
                        hidden gems, cultural hotspots, must-visit landmarks, weather forecasts, and high-level costs.

                    **Parameters**:
                    - City: {city}
                    - Interests: {interests}
                    - Travel Date: {travel_dates}

                    **Note**: {self.__tip_section()}
            """
            ),
            agent=agent,
            expected_output=dedent(
                """
                A comprehensive city guide in markdown format.
                The guide must contain:
                - A section on local customs and etiquette.
                - A list of at least 3 special events or festivals happening during the travel dates.
                - A list of 10 recommended activities, categorized by the traveler's interests.
                - A summary of expected costs for food, transport, and attractions.
                """
            ),
        )