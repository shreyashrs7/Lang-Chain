from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt1 = PromptTemplate(
    template= "Generate  a tweet about a {topic}",
    input_variables= ['topic']
)


prompt2 = PromptTemplate(
    template= "Generate a Linkedin post about {topic}",
    input_variables= ['topic']
)

parser = StrOutputParser()


parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'Linkedin' : RunnableSequence(prompt2, model, parser)
})

result = parallel_chain.invoke({'topic': 'AI'})

#print(result)

print(result['tweet'])
print(result['Linkedin'])