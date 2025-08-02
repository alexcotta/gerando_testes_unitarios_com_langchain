from langchain_experimental.utilities import PythonREPL
from langchain.chat_models import ChatOpenAI

# Configuração do modelo ChatGPT da OpenAI via LangChain
chatgpt = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Instancia o Python REPL do LangChain
python_repl = PythonREPL()
