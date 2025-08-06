from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableLambda, RunnableParallel, RunnablePassthrough

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def word_count(text):
    return len(text.split())

prompt = PromptTemplate(
    template= "write a joke about {topic}",
    input_variables= ['topic']
)

parser = StrOutputParser()

joke_chain = RunnableSequence(prompt, model, parser)

parallel_cahin = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_chain, parallel_cahin)

result = final_chain.invoke({'topic': 'Computer'})

final_result = """{} \n word count - {}""".format(result['joke'], result['word_count'])

print(final_result)