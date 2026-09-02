# from google.adk.agents.llm_agent import Agent

# def get_login_troubleshooting_steps(issue_type: str) -> dict:
#     """Provides exact troubleshooting steps for login, password, and 2FA issues in Velocity.

#     Args:
#         issue_type (str): The specific problem ('forgot_password', 'no_reset_email', '2fa_code_delayed', 'account_locked','account_subscription_expired')

#     Returns:
#         dict: Clear, step-by-step resolution instructions for the user.
#     """
#     issue = issue_type.lower().strip()

#     guides = {
#         "forgot_password": {
#             "title": "Resetting Your Password",
#             "steps": [
#                 "1. Go to the main Velocity login screen.",
#                 "2. Click the 'Forgot Password?' link below the login box.",
#                 "3. Enter your registered business email address and submit.",
#                 "4. Check your inbox for the reset link (check Spam/Junk if missing).",
#             ],
#         },
#         "no_reset_email": {
#             "title": "Password Reset Email Not Arriving",
#             "steps": [
#                 "1. Wait up to 5 minutes and refresh your inbox.",
#                 "2. Check your Spam, Junk, or Clutter folders.",
#                 "3. Confirm that the email you have on velocity is correctly linked to your account give a direct call"
#             ],
#         },
#         "2fa_code_delayed": {
#             "title": "2FA / SMS Code Delays",
#             "steps": [
#                 "1. We recommend installing the twilio authentication application",
#                 "2. If using an authenticator app, ensure your phone's clock auto-sync setting is turned ON.",
#             ],
#         },
#         "account_locked": {
#             "title": "account locked message showing up",
#             "steps": [
#                 "1. For the account lock reach out to your admin office and ask them to send a request to newton customer care to reactivate your account"
#             ]
#         },
#         "account_subscription_expired" : {
#             "title": "Account Subscription expired message",
#             "steps":[
#                 "1. Reach directly to customer care to get your subscription renewe d and provide the username email and firm name to ensure it is resolved effectively"
#             ]
#         }
#     }

#     return guides.get(
#         issue,
#         {
#             "status": "unknown_issue",
#             "message": "For general login issues, try clearing your browser cache or opening Velocity in an Incognito window and if the issue persist contact newton customer care",
#         },
#     )
# def get_mortgage_details_guide(issue_type: str)-> dict:
#     '''
#     Provides the solution for the user facing issue with filling mortgage
#     Args:
#      issue_types(str): The specific problem('Second_mortgage')
#     Returns:
#      dict: Clear, step-by-step resolution instructions for the user.
#     '''
#     issue = issue_type.lower().strip()
    
#     guides = {
#            "Second_mortgage":{
#                "Title": ""
#            }
#         }
# def application_filling_error(issue_type: str)-> dict:
#     '''
#     Provide the solution to user facing issue with the filling the applicaton or files
#     Args: 
#     issue_type (str): The specific problem ()
#     '''
from google.adk.agents.llm_agent import Agent
from knowledge_serach import search_knowledge

root_agent = Agent(
    model='gemini-3.5-flash',
    name="velocity_support_agent",
    description="Tier-1 customer support assistant for Velocity by Newton Connectivity Systems.",
    instruction=(
    "You are 'Velocity Support AI', a customer care assistant for Velocity (Newton Connectivity Systems).\n\n"

    "STRICT KNOWLEDGE RULES:\n"
    "1. You MUST use the search_knowledge tool to find relevant information for Velocity support questions.\n"
    "2. You MUST ONLY provide support steps that are supported by the information returned by search_knowledge.\n"
    "3. NEVER make up, assume, or guess software policies, features, or restrictions that are not present in the retrieved knowledge.\n"
    "4. Use the retrieved knowledge to answer clearly and concisely. Do not repeat unnecessary information or unrelated content.\n"
    "5. If the knowledge base does not contain the answer, clearly state that you don't have the exact steps for that issue in your knowledge base yet, and recommend contacting Newton Customer Care directly.\n"
    ),
    tools=[search_knowledge],
)
