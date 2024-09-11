import os

import uvicorn
from lanarky import Lanarky
from lanarky.adapters.openai.resources import ChatCompletionResource
from lanarky.adapters.openai.routing import OpenAIAPIRouter

# Set the OPENAI_API_KEY environment variable in your shell
# or pass it to through the following line
os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")

app = Lanarky()
router = OpenAIAPIRouter()


@router.post("/chat")
def chat(stream: bool = True) -> ChatCompletionResource:
    system = "Here is you assistant"
    return ChatCompletionResource(stream=stream, system=system)


if __name__ == "__main__":
    app.include_router(router)
    uvicorn.run(app)
