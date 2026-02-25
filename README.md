# SDLC Architect Agent

An AI-powered agent that generates professional High-Level Design (HLD) documents based on user stories and requirements using Google's Gemini 2.5 Flash model.

## Overview

The SDLC Architect Agent is a sophisticated software architecture assistant that leverages Google's Agent Development Kit (ADK) and Gemini AI to create comprehensive High-Level Design documents. The agent follows structured templates and industry best practices to produce detailed architectural specifications including system overview, functional/non-functional requirements, data architecture, deployment strategies, and security considerations.

## Features

- **Template-Driven Design**: Uses customizable Word document templates for consistent HLD structure
- **AI-Powered Generation**: Leverages Google Gemini 2.5 Flash for intelligent architectural recommendations
- **Cloud Provider Analysis**: Automatically analyzes requirements and recommends optimal cloud providers (GCP, AWS, Azure)
- **Diagram Generation**: Creates Graphviz DOT notation diagrams for system architecture visualization
- **Comprehensive Coverage**: Addresses all aspects of software architecture including security, scalability, and compliance

## Architecture

### Core Components

- **Agent Framework**: Built on Google ADK for robust agent lifecycle management
- **Template Engine**: Dynamic loading of HLD templates from Word documents
- **AI Integration**: Seamless integration with Google GenAI for LLM capabilities
- **Document Processing**: Support for .docx template parsing and content extraction

### Key Files

- `agent.py`: Main agent implementation with HLD generation logic
- `templates/hld_template.docx`: Customizable HLD template structure
- `requirements.txt`: Python dependencies and package specifications
- `.env`: Environment configuration (Google Cloud Project ID, API keys)

## Prerequisites

### Google Cloud Setup

1. **Google Cloud Project**: Create or use an existing GCP project
2. **Authentication**: Run `gcloud auth application-default login` in your terminal
3. **API Enablement**: Enable the Gemini API and required Google Cloud services
4. **Environment Variables**: Set `GOOGLE_CLOUD_PROJECT` in your `.env` file

### Python Environment

- Python 3.8 or higher
- pip package manager

## Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd Architect_Agent
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**
   ```bash
   # Create .env file with all required variables
   echo "GOOGLE_CLOUD_PROJECT=your-project-id" > .env
   echo "GOOGLE_CLOUD_LOCATION=us-central1" >> .env
   echo "GOOGLE_GENAI_USE_VERTEXAI=true" >> .env
   ```

## Usage

### Running the Agent

Execute the agent using the ADK web interface:

```bash
adk web 
```

This will start the ADK web server where you can interact with the Architect Agent through a browser interface.

### Customization

#### Modifying User Stories

Edit the `USER_STORIES` constant in `agent.py` to include your specific requirements:

```python
USER_STORIES = """
[STORY-001] Your requirement description
[STORY-002] Another requirement
"""
```

#### Custom HLD Templates

1. Create or modify `templates/hld_template.docx` with your desired structure
2. The agent will automatically load and follow your template hierarchy
3. Ensure sections are clearly defined with proper headings

### Output Format

The agent generates:
- **Structured HLD Document**: Following your template's exact hierarchy
- **Architecture Diagrams**: Graphviz DOT notation for system visualization
- **Cloud Recommendations**: Justified provider selection based on requirements
- **Comprehensive Coverage**: All architectural aspects from functional to security

## Dependencies

### Core Framework
- `google-adk`: Google Agent Development Kit
- `google-genai`: Google Generative AI SDK

### Document Processing
- `python-docx`: Word document manipulation
- `markdown`: Markdown processing support

### Utilities
- `requests`: HTTP client for API interactions
- `python-dotenv`: Environment variable management
- `graphviz`: Diagram generation and rendering

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `GOOGLE_CLOUD_PROJECT` | GCP Project ID | `your-project-id` |
| `GOOGLE_CLOUD_LOCATION` | GCP region for resources | `us-central1` |
| `GOOGLE_GENAI_USE_VERTEXAI` | Use Vertex AI endpoint | `true` |

### Agent Configuration

- **Model**: Gemini 2.5 Flash (`gemini-2.5-flash`)
- **Location**: `us-central1`

## Template Structure

The agent expects HLD templates to include these standard sections:

1. **Introduction** (Purpose, Scope, Audience, Project Context)
2. **System Overview** (Conceptual Architecture, Style, Principles)
3. **Functional Architecture** (Core Services, Data Ingestion, UI/UX)
4. **Non-Functional Architecture** (Performance, Scalability, Security, Reliability)
5. **Data Architecture Strategy** (Logical Model, Storage, Data Flow)
6. **Deployment Architecture** (Cloud Strategy, Containerization, CI/CD)
7. **Security Architecture** (IAM, Data Protection, Network Security)
8. **Cross-Cutting Concerns** (Error Handling, Monitoring, Observability)
9. **Future Considerations**
10. **Open Issues / TBDs**

## Example Output

The agent produces professional HLD documents with:

- **Detailed Analysis**: Comprehensive breakdown of system requirements
- **Visual Diagrams**: Graphviz-based architecture diagrams
- **Cloud Strategy**: Justified recommendations with specific services
- **Implementation Guidance**: Practical considerations for development teams

## Development

### Project Structure

```
Architect_Agent/
├── agent.py              # Main agent implementation
├── requirements.txt      # Python dependencies
├── .env                 # Environment configuration
├── .gitignore          # Git ignore rules
├── templates/           # HLD template directory
│   └── hld_template.docx # Default HLD template
└── README.md           # This documentation
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Troubleshooting

### Common Issues

1. **Authentication Errors**: Ensure `gcloud auth application-default login` is run
2. **Template Not Found**: Verify `templates/hld_template.docx` exists
3. **Project ID Issues**: Check `GOOGLE_CLOUD_PROJECT` in `.env` file
4. **API Access**: Confirm Gemini API is enabled in your GCP project

### Debug Mode

Enable verbose logging by modifying the agent configuration or checking the `.adk/` directory for session logs.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:
- Check the troubleshooting section
- Review Google ADK documentation
- Consult Gemini API documentation
- Create an issue in the repository

## Version History

- **v1.0.0**: Initial release with template-driven HLD generation
- Support for Google Gemini 2.5 Flash
- Word document template integration
- Cloud provider analysis and recommendations