from backend.tools.get_datetime import get_datetime

TOOL_DEFINITIONS = [
    {
        "type": "function",
        "function": {
            "name": "get_datetime",
            "description": (
                "Return the current date and time from the backend. "
                "Use this when the user asks for the current date, time, or both."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        },
    },
]

TOOL_FUNCTIONS = {
    "get_datetime": lambda _args: get_datetime(),
}
