# Streamlit LLM Chat Template

This repository contains a template for building a Streamlit application that integrates with a large language model (LLM) for conversational interactions. The template uses the `langchain_anthropic` library to interface with the Claude-3-5-sonnet-20240620 model from Anthropic.

## Introduction

The Streamlit LLM Chat Template provides a simple and intuitive user interface for engaging in conversational interactions with a powerful language model. Users can type their prompts or questions into the chat input field, and the application will stream the model's response in real-time.

This template serves as a starting point for building more complex applications that leverage the capabilities of large language models. It can be easily extended and customized to suit specific use cases, such as question-answering, text generation, or task completion.

## Installation

To run the Streamlit LLM Chat Template locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your-username/streamlit-llm-chat-template.git
```

2. Navigate to the project directory:

```bash
cd streamlit-llm-chat-template
```

3. Create a virtual environment and activate it:

```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Set up the required environment variables by creating a `.env` file in the project root directory with the following content:

```
ANTHROPIC_API_KEY=your_anthropic_api_key
```

Replace `your_anthropic_api_key` with your actual Anthropic API key.

## Usage

To run the Streamlit application, execute the following command:

```bash
streamlit run main.py
```

This will start the Streamlit server and open the application in your default web browser. You can then interact with the chat interface by typing your prompts or questions and observing the model's responses.

## Contributing

Contributions to the Streamlit LLM Chat Template are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

When contributing, please follow these guidelines:

1. Fork the repository and create a new branch for your feature or bug fix.
2. Make your changes and ensure that the code follows best practices and is well-documented.
3. Test your changes thoroughly.
4. Submit a pull request with a clear description of your changes and their purpose.

## License

This project is licensed under the [MIT License](LICENSE).