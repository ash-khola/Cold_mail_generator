## 🧊 Cold Mail Generator

**Cold Mail Generator** A cold email generator built for service-based companies, utilizing GROQ, LangChain, and Streamlit. Users can input a company’s careers page URL, after which the tool automatically scrapes job listings from the site. It then generates personalized cold emails tailored to those roles, including portfolio links that are smartly fetched from a vector database based on the job descriptions.

---

## 📦 Tech Stack

- Llama3.1(open sournce LLM)
- chromadb(vector store)
- Langchain
- Streamlit

---

## 🧩 Architecture Diagram

![image](https://github.com/user-attachments/assets/a229b8bb-9db1-411c-b4e6-a8ee4465e12d)


## 🛠️ Set-up

1. **Get your API key**  
   First, obtain an API key from [Groq Console](https://console.groq.com/keys).  
   Then, inside the `app/.env` file, update the value of `GROQ_API_KEY` with the API key you generated.

2. **Install dependencies**  
   Use the following command to install all required packages:

   ```bash
   pip install -r requirements.txt

3. **Run the Streamlit app**

   ```bash
   streamlit run app/main.py
