# Project Description

The aim of this self-initiated project is to analyze media for any harmful content that may be of danger to Singapore's society. Its inception is based on recent news that there were multiple teenagers in Singapore being detained by our Internal Security Department (ISD) for radcialized remarks or extremist actions made by them. Upon their individual assessment by the ISD, it is noted that these teenagers had been watching content online that distorts their beliefs of other religion without supervision. Thus, this project is initiated to propose a framework that ensures peace, harmony and security of our country by making available to everyone a means to validate content that does not disturb Singapore's peaceful and harmonious environment and that does not violate any Singapore law.

# Project Layout

This website shall utilize Large Language Models (LLMs) as agents to assess multiple forms of media. The center of the agentic brain shall be OpenAI's `gpt-5.4-mini` model, while other models from various sources shall be used for visual and aural understanding, such as Google's `gemini-3.5-flash` model for video understanding and YouTube video compatibility, and OpenAI's `gpt-transcribe` model for aural transcripiton. A separate open-weights model, `qwen-3-vl`, shall be used for fine-tuning based on chat history by multiple users. The chat history shall be saved in a database for summary transcription between the users and the agent, which will then be used for fine-tuning for Qwen's model for internal use.

# Chat flow

The user shall be able to prompt the agent like an ordinary chatbot, where it could take in multiple forms of content, such as texts, images, videos and audio files. As the user inputs a prompt with regards to the content they are watching, the agent shall decide which agents as tools to use in the event it is not compatible with formats like videos or audios. The tools shall transcribe (and describe) the content and shall also use other tools to decide if the content is harmful or not. This evaluation shall be passed back to the main agent to summarize the results and return an answer to the user with regards to the content submitted.

The graph below shows the flow of such orchestration:

<!-- insert your drawing here -->

Should a content be flagged as harmful by the agent when conditions are met, the agent would prepare an email to relevant parties regarding the content either for further scrutiny of users' behaviour or for videos to be put down by the first party developers. This ensures 

# Fine-tuning of `qwen-3-vl` model

The purpose of fine-tuning `qwen-3-vl` model is to rely less on cloud services while retaining similar capabilities of all agents involved in one local, lightweight model for further privacy, as data of such conversation could be embarrassing to the users or could be used against them should their conversations be accessible to wrong external parties. 