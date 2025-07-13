import typer
from typer import Option
from datetime import datetime


app = typer.Typer()

@app.command()
def suggest(
        day: str = Option(..., "--day", "-d", help= "Day to check (e.g. 'Saturday')"),
        location: str= Option(..., "--location", "-l", help= "Location for weather check")
            ):
    """
    Suggest activities based on the day and location's weather.
    """

    typer.echo(f"Fetching weather for {location} on {day}...")
    # TODO: Call weather_service + activity_planner
    # TODO: Logic control for better user experiment
    typer.echo("Suggested: Picnic at Tiergarten 🧺")

@app.command()
def add_event(title: str, datetime_str: str):
    """
    Add a new event to your location
    """
    try:
        dt = datetime.fromisoformat(datetime_str)
        # TODO: Call calendar_manager.add_event(title, dt)
        # TODO: Logic control for better user experiment
        typer.echo(f"Added event: {title} at {dt}")
    except ValuerError:
        typer.echo("❌ invalid datetime format. Use YYYY-MM-DDTHH:MM")

@app.command()
def show_scedule():
    """
    Show upcoming events.
    """
    # TODO: Fetch from calendar
    # TODO: Logic Control for better user experiment
    typer.echo("Your upcoming events \n -Gym - 2025-07-10 09:00")

@app.command()
def plan_with_ai(prompt: str):
    """
    Generate activity with AI from a prompt.
    """
    typer.echo(f"🤖Interpreting: {prompt}")
    # TODO: Call ai_assistant.generate_plan(prompt) -> title + date should be in the prompt
    # TODO: Call calendar_manger.add_event(title, dt)
    # TODO: Logic contorl for better prompt from user to the model
    typer.echo("AI Suggestion: 'Relaxing walk in the partk on Sunday' added!")

if __name__ == "__main__":
    app()
