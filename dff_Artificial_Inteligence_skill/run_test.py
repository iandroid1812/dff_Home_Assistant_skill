import random

from scenario.main import actor
from helper_functions.requesting import weather_forecast_request
import run_interactive

random.seed(314)

# testing
data = weather_forecast_request()
degree = u'\N{DEGREE SIGN}'

testing_dialog = [
    ("Hi",
     "Hello, I am your Home Assistant. How can I help?"
     ),
    ("Please, tell me about the weather.",
     f"The temperature in {data['loc']} is {data['temp']}{degree}C. It feels like {data['feels-like']}{degree}C." \
     "\nDo you want to get more information?"
     ),
    ("Ok",
     f"Weather report: {data['report']}. The humidity level is {data['humidity']}% " \
     f"and the wind speed is {data['wind']} m/s."
     ),
    ("Great, thank you!",
     "Glad I could help!"),

    # end of convo 1
    ("", None),

    ("HEY",
     "Hello, I am your Home Assistant. How can I help?"
     ),
    ("Whats the weather outside?",
     f"The temperature in {data['loc']} is {data['temp']}{degree}C. It feels like {data['feels-like']}{degree}C." \
     "\nDo you want to get more information?"
     ),
    ("Nope",
     "Ok, that's it for the weather then."),

    # end of convo 2
    ("", "Awaiting for commands..."),

    ("Hello",
     "Hello, I am your Home Assistant. How can I help?"
     ),
    ("Turn on the lights please.",
     "Ok, in which room?"),
    ("In the garage",
     "Ok, in which room?"),
    ("The bedroom",
     "Turned on the lights in the bedroom"),
    ("",
     "Do you want to dim the light as well?"),
    ("ok",
     "What brightness do you want?"),
    ("Let's dim to 25%",
     "Dimmed the light in the bedroom to 25%"),
    ("Good job",
     "Glad I could help!"),

    # end of convo 3
    ("", "Awaiting for commands..."),

    ("Hello",
     "Hello, I am your Home Assistant. How can I help?"),
    ("Please set the temperature to 29 degreed in the hall.",
     "Set the temperature in the hall to 29 degrees"),
    ("good job",
     "Glad I could help!"),

    # end of convo 4
    ("", "Awaiting for commands...")
]


def run_test():
    ctx = {}
    for in_request, true_out_response in testing_dialog:
        _, ctx = run_interactive.turn_handler(in_request, ctx, actor, true_out_response=true_out_response)
    print("test passed")


if __name__ == "__main__":
    run_test()
