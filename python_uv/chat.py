import logging
from logging import getLogger

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

logger = getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


def chat() -> None:
    """Chat with gpt-4o chat."""
    llm = ChatOpenAI(model="gpt-4o-mini")
    response = llm.invoke("こんにちは。私は元気です。")
    logger.debug(response.content)


if __name__ == "__main__":
    chat()
