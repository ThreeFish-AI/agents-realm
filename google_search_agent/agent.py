from google.adk.agents import Agent
from google.adk.tools import google_search

# 注意：请根据“Supported models”段落确认 Live API 模型 ID
root_agent = Agent(
    name="basic_search_agent",
    model="gemini-2.0-flash-live-001",  # 示例，可替换为最新可用 Live 模型
    description="Agent to answer questions using Google Search.",
    instruction="You are an expert researcher. You always stick to the facts.",
    tools=[google_search],
)
