from fastapi import APIRouter
from pydantic import BaseModel
import logging

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from my_agent.agent import root_agent

router = APIRouter()
logger = logging.getLogger("uvicorn.error")
logger.setLevel(logging.DEBUG)

session_service = InMemorySessionService()

runner = Runner(
    app_name="velocity_support_agent",
    agent=root_agent,
    session_service=session_service,
)

class Question(BaseModel):
    question: str


@router.post("/ask")
async def ask(question: Question):
    logger.debug("question recevied", question.question)
    session = await session_service.create_session(
        app_name="velocity_support_agent",
        user_id="user",
    )

    message = types.Content(
        role="user",
        parts=[types.Part.from_text(text=question.question)],
    )

    answer = None

    async for event in runner.run_async(
        user_id=session.user_id,
        session_id=session.id,
        new_message=message,
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                answer = event.content.parts[0].text

    return {
        "answer": answer
    }


@router.get("/test")
def test():
    logger.debug("~~~ HELLO FROM THE ROUTE ~~~")
    return "hello from the router"

# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel
# from google.adk.runners import Runner
# from google.adk.sessions import InMemorySessionService
# from backend.app.agent_package.main_agent import root_agent

# router = APIRouter(prefix="/ask", tags=["Ask"])

# # InMemorySessionService keeps conversation context linked to session IDs in RAM
# session_service = InMemorySessionService()
# runner = Runner(agent=root_agent, session_service=session_service)

# class QueryRequest(BaseModel):
#     user_id: str = "user_123"
#     session_id: str  # Mandatory for maintaining chat history
#     message: str

# @router.post("")
# async def ask_agent(payload: QueryRequest):
#     try:
#         # 1. Fetch or create the session state in ADK
#         session = await session_service.get_or_create_session(
#             app_name="velocity_app",
#             user_id=payload.user_id,
#             session_id=payload.session_id
#         )

#         # 2. Run agent turn - ADK attaches conversation history automatically
#         result = await runner.run_async(
#             user_id=payload.user_id,
#             session_id=session.id,
#             new_message=payload.message
#         )

#         return {
#             "session_id": session.id,
#             "response": str(result.text)
#         }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))