# CrewAI Trip Planner

This project is a simple AI-powered trip planner that leverages the CrewAI framework to generate detailed travel itineraries. It orchestrates a crew of specialized AI agents to collaborate and fulfill the task of planning a 7-day trip based on user preferences.

## Features

* **Intelligent Itinerary Generation:** Creates comprehensive 7-day travel plans, including daily activities, weather forecasts, dining suggestions, packing lists, and budget breakdowns.
* **City Selection:** Identifies optimal travel destinations considering factors like weather patterns, seasonal events, and travel costs.
* **In-depth City Guides:** Compiles detailed information about selected cities, covering attractions, local customs, special events, and high-level cost estimates.
* **Dynamic Tool Utilization:** Integrates with external tools for real-time information retrieval and calculations.

## How It Works

The trip planner operates using a crew of three distinct AI agents, each with a specific role and set of responsibilities:

### Agents

* **Expert Travel Agent**
    * **Role:** Expert in travel planning and logistics.
    * **Goal:** To create a detailed 7-day travel itinerary including budget, packing suggestions, and safety tips.
    * **Tools:** Utilizes the "Search the internet" tool (for general information) and the "Make a calculation" tool (for budget calculations).
* **City Selection Expert**
    * **Role:** Expert at analyzing travel data to pick ideal destinations.
    * **Goal:** To select the best cities based on weather, season, prices, and traveler interests.
    * **Tools:** Employs the "Search the internet" tool for data analysis.
* **Local Tour Guide**
    * **Role:** Knowledgeable local guide with extensive information about the city, its attractions, and customs.
    * **Goal:** To provide the best insights about the selected city.
    * **Tools:** Uses the "Search the internet" tool to gather in-depth city information.

### Tasks

The agents collaborate to complete the following tasks:

* **Identify Best City for the Trip:** The `City Selection Expert` analyzes criteria such as weather, seasonal events, and travel costs to recommend a single best city. The output is a detailed report including flight costs, weather forecasts, and attractions.
* **Gather In-depth City Guide Information:** The `Local Tour Guide` compiles a comprehensive guide for the chosen city, covering attractions, local customs, special events, and daily activity recommendations.
* **Plan 7-Day Travel Itinerary:** The `Expert Travel Agent` develops a full 7-day itinerary with per-day plans, including places to eat, packing suggestions, and a budget breakdown, leveraging information from the city guide.

### Tools

The project utilizes custom tools to enhance the agents' capabilities:

* **Search the internet** (`SearchTool`): This tool is used by agents to search the internet for information on a given topic. It retrieves and returns relevant results including titles, links, and snippets. It requires a `SERPER_API_KEY` to function.
* **Make a calculation** (`CalculatorTool`): This tool allows agents to perform mathematical calculations based on a given expression.

## Project Structure

* `agents.py`: Defines the roles, goals, backstories, and tools for each AI agent.
* `tasks.py`: Defines the specific tasks the agents need to perform, including their descriptions and expected outputs.
* `main.py`: The main script that initializes the CrewAI framework, instantiates the agents and tasks, and kicks off the autonomous crew to generate the trip plan.
* `tools/`: Directory containing custom tools:
    * `search_tools.py`: Implements the `SearchTool` for internet searches.
    * `calculator_tools.py`: Implements the `CalculatorTool` for mathematical calculations.
* `pyproject.toml`: Project metadata and dependencies.
* `poetry.lock`: Poetry lock file for dependency management.
* `.gitignore`: Specifies intentionally untracked files to ignore.
* `README.md`: This file.

## Technologies Used

* Python 3.10+
* [CrewAI](https://docs.crewai.com/)
* [CrewAI-Tools](https://github.com/joaomdmoura/crewai-tools)
* `python-dotenv`
* `unstructured`
* `pyowm`

## Setup

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/ramanuja-5194/crewai-trip_planner.git](https://github.com/ramanuja-5194/crewai-trip_planner.git)
    cd crewai-trip_planner
    ```

2.  **Install dependencies using Poetry:**

    If you don't have Poetry installed, follow the instructions on the [Poetry website](https://python-poetry.org/docs/#installation).

    ```bash
    poetry install
    ```

3.  **Set up environment variables:**

    Create a `.env` file in the root directory of the project and add your API keys:

    ```
    SERPER_API_KEY="your_serper_api_key_here"
    # Add any other API keys required by your LLM provider (e.g., OPENAI_API_KEY, GEMINI_API_KEY)
    # Example for OpenAI:
    # OPENAI_API_KEY="your_openai_api_key"
    # Example for Gemini (used in this project):
    # GEMINI_API_KEY="your_gemini_api_key"
    ```
    The project uses `gemini/gemini-1.5-flash` model, so you need a Google Gemini API key configured as `GEMINI_API_KEY` in your `.env` file.
    You can get your Serper API Key from [Serper.dev](https://serper.dev/) and your Google Gemini API Key from [Google AI Studio](https://aistudio.google.com/app/apikey).

## How to Run

1.  **Activate the Poetry shell:**

    ```bash
    poetry shell
    ```

2.  **Run the main script:**

    ```bash
    python main.py
    ```

    The script will prompt you to enter details about your trip, such as your origin, desired cities, date range, and interests.

## Example Usage