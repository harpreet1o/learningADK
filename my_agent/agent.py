from google.adk.agents.llm_agent import Agent
import datetime

def get_current_time(timezone_name: str = "UTC")->dict:
    """
    Get the current time in the specified timezone.

    Args:
        timezone_name (str): The name of the timezone. Defaults to "UTC".

    Returns:
        dict: A dictionary containing the current time and timezone.
    """
    try:
        # Get the current time in the specified timezone
        tz = datetime.timezone(datetime.timedelta(hours=int(timezone_name.split('/')[-1])))
        current_time = datetime.datetime.now(tz)
        return {
            "current_time": current_time.strftime("%Y-%m-%d %H:%M:%S"),
            "timezone": timezone_name
        }
    except Exception as e:
        return {
            "error": str(e)
        }
def get_weather(city: str)->str:
        """
        Get the current weather for a city.
        Args:
         city(str): The weather in the city.

        Returns:
         str: A string containing the today's weather.
        """
        try:
            weather= "always sunny"
            return weather
        except Exception as e:
                return {
                    "error": str(e)
                }

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    tools=[get_current_time, get_weather],
)
