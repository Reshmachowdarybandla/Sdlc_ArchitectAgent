# import os
# import asyncio
# from google.adk.agents import Agent
# from google.adk.runners import Runner
# from google.adk.sessions import InMemorySessionService
# # Using genai types as they are the most stable for ADK/Gemini 1.5 Pro
# from google.genai import types

# # --- 1. Configuration ---
# # Ensure you have run 'gcloud auth application-default login' in your terminal
# PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT", "your-project-id")
# LOCATION = "us-central1"
# MODEL_NAME = f"projects/{PROJECT_ID}/locations/{LOCATION}/publishers/google/models/gemini-2.5-flash"

# # --- 2. HLD System Instructions (Based on your Word Template) ---
# HLD_SYSTEM_PROMPT = """
# You are a Senior Software Architect. Your goal is to generate a professional High-Level Design (HLD).
# STRICTLY follow this section hierarchy from the provided standard template:

# 1. Introduction (Purpose, Scope, Audience, Project Context)
# 2. System Overview (Conceptual Architecture Diagram, Style, Principles)
# 3. Functional Architecture (Core Services, Data Ingestion, UI/UX)
# 4. Non-Functional Architecture (Performance, Scalability, Security, Reliability)
# 5. Data Architecture Strategy (Logical Model, Storage, Data Flow)
# 6. Deployment Architecture (Cloud Strategy, Containerization, CI/CD)
# 7. Security Architecture (IAM, Data Protection, Network Security)
# 8. Cross-Cutting Concerns (Error Handling, Monitoring, Observability)
# 9. Future Considerations
# 10. Open Issues / TBDs

# DIAGRAM REQUIREMENTS:
# - Use Graphviz DOT notation within ```graphviz:dot code blocks.
# - Include a conceptual runtime diagram in Section 2.1.

# CLOUD LOGIC:
# - Analyze user stories and suggest the best cloud provider (GCP, AWS, or Azure) based on requirements.
# """

# # --- 3. Agent Definition ---
# # CRITICAL: Variable must be named 'root_agent' for the ADK CLI to discover it
# root_agent = Agent(
#     name="Architect_Agent",
#     model=MODEL_NAME,
#     instruction=HLD_SYSTEM_PROMPT
# )

# # --- 4. Hardcoded User Stories ---
# USER_STORIES = """
# [STORY-001] Secure Authentication: Users must authenticate via corporate SSO with MFA.
# [STORY-002] IoT Data Ingestion: System must ingest 50,000 telemetry events per second.
# [STORY-003] Compliance Storage: Processed data must be archived in cold storage for 5 years.
# """

# # --- 5. Execution Logic ---
# async def generate_hld():
#     session_service = InMemorySessionService()
#     runner = Runner(agent=root_agent, session_service=session_service)
    
#     prompt = f"Please generate a complete HLD based on these user stories:\n{USER_STORIES}"
    
#     # Using types.Content and types.Part to ensure compatibility
#     events = runner.run(
#         session_id="test_session_001",
#         user_id="Reshma",
#         input=types.Content(
#             role="user", 
#             parts=[types.Part(text=prompt)]
#         )
#     )
    
#     print("\n--- GENERATED HLD ---\n")
#     for event in events:
#         if hasattr(event, 'text') and event.text:
#             print(event.text, end="")

# if __name__ == "__main__":
#     asyncio.run(generate_hld())




import os
import asyncio
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# --- 1. Configuration ---
PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT", "your-project-id")
LOCATION = "us-central1"
MODEL_NAME = f"projects/{PROJECT_ID}/locations/{LOCATION}/publishers/google/models/gemini-2.5-flash"


import docx  # New import for Word support

def load_hld_template(template_filename: str = "hld_template.docx") -> str:
    """
    Loads text from a .docx HLD template from the 'templates' folder.
    """
    # Resolves path to your .docx file
    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(base_dir, "templates", template_filename)

    if not os.path.exists(template_path):
        raise FileNotFoundError(
            f"HLD template not found at: {template_path}\n"
            f"Please ensure your Word file exists inside the 'templates/' folder."
        )

    # Logic to extract text from Word paragraphs
    try:
        doc = docx.Document(template_path)
        # Collects text from every paragraph in the Word doc
        full_text = [para.text for para in doc.paragraphs]
        return "\n".join(full_text)
    except Exception as e:
        raise RuntimeError(f"Failed to read the .docx file: {e}")

# --- 3. Base System Instructions (no hardcoded structure) ---
BASE_SYSTEM_PROMPT = """
You are a Senior Software Architect. Your goal is to generate a professional High-Level Design (HLD) document.

STRICT RULES:
- You MUST follow the exact section hierarchy, headings, and structure defined in the HLD Template provided below.
- Do NOT add, remove, or reorder sections beyond what the template defines.
- Populate every section with content relevant to the provided user stories.
- Leave a section as "TBD" only if there is genuinely no information to derive from the user stories.

DIAGRAM REQUIREMENTS:
- Use Graphviz DOT notation within ```graphviz:dot code blocks.
- Include a conceptual runtime architecture diagram in the System Overview section.

CLOUD LOGIC:
- Analyze the user stories and recommend the most suitable cloud provider (GCP, AWS, or Azure) with justification.

--- HLD TEMPLATE START ---
{hld_template}
--- HLD TEMPLATE END ---
"""

# --- 4. Agent Factory (template injected at startup) ---
def create_agent() -> Agent:
    """Creates the Architect Agent with the HLD template baked into its instructions."""
    hld_template = load_hld_template()
    system_prompt = BASE_SYSTEM_PROMPT.format(hld_template=hld_template)

    return Agent(
        name="Architect_Agent",
        model=MODEL_NAME,
        instruction=system_prompt
    )

# ADK CLI requires a module-level 'root_agent' — we build it once at import time
root_agent = create_agent()

# --- 5. Hardcoded User Stories ---
USER_STORIES = """
[STORY-001] Secure Authentication: Users must authenticate via corporate SSO with MFA.
[STORY-002] IoT Data Ingestion: System must ingest 50,000 telemetry events per second.
[STORY-003] Compliance Storage: Processed data must be archived in cold storage for 5 years.
"""

# --- 6. Execution Logic ---
async def generate_hld():
    session_service = InMemorySessionService()
    runner = Runner(agent=root_agent, session_service=session_service)

    prompt = f"Please generate a complete HLD based on these user stories:\n{USER_STORIES}"

    events = runner.run(
        session_id="test_session_001",
        user_id="Reshma",
        input=types.Content(
            role="user",
            parts=[types.Part(text=prompt)]
        )
    )

    print("\n--- GENERATED HLD ---\n")
    for event in events:
        if hasattr(event, 'text') and event.text:
            print(event.text, end="")

if __name__ == "__main__":
    asyncio.run(generate_hld())
