# Ben's Dotfiles

This repository contains my personal dotfiles and development environment configuration, managed with [chezmoi](https://www.chezmoi.io/).

## 🚀 Quick Start

### Install on a new machine

```bash
# Install chezmoi and apply dotfiles in one command
sh -c "$(curl -fsLS get.chezmoi.io)" -- init --apply benpchandler
```

### Manual installation

```bash
# Install chezmoi (macOS with Homebrew)
brew install chezmoi

# Initialize and apply dotfiles
chezmoi init benpchandler
chezmoi apply
```

## 📁 What's Included

### Development Tools

- **Shell Configuration**
  - Zsh configuration with Oh My Zsh
  - Powerlevel10k theme
  - Custom aliases and functions

- **Git Configuration**
  - Global gitconfig with HTTPS authentication
  - Commit message templates
  - Useful aliases

- **VS Code Settings**
  - Extensions configuration
  - Keybindings
  - User settings

### Project-Specific Configurations

- **QoE App** (`Dev/QoE_App/`)
  - `.claude/` - Claude AI assistant custom commands
  - Project-specific CLAUDE.md for AI context
  - Development environment settings

### MCP (Model Context Protocol) Configuration

- Shared MCP configuration at `~/.mcp.json`
- Symlinked to project directories as needed
- Contains AI model server configurations

## 🛠️ Usage

### Common Commands

```bash
# See what changes chezmoi would make
chezmoi diff

# Apply changes from the repository
chezmoi apply

# Update dotfiles from the repository
chezmoi update

# Add a new file to be managed
chezmoi add ~/.config/newfile

# Edit a managed file
chezmoi edit ~/.zshrc

# See all managed files
chezmoi managed
```

### Managing Project-Specific Files

```bash
# Add project files (like .claude folders)
cd /path/to/project
chezmoi add -r .claude/

# The files will be stored with 'dot_' prefix in the source
# e.g., .claude/ becomes dot_claude/ in the repository
```

### Working with Templates

This repository includes project templates that can be used to scaffold new projects:

```bash
# Create a new Python + React full-stack project
cookiecutter templates/python-react-app/

# Create a new Python backend API with vertical slice architecture
cookiecutter templates/python-backend/
```

Available templates:

#### python-backend
A modern Python backend template featuring:
- **FastAPI** with REST + GraphQL support
- **Vertical Slice Architecture** - feature-based organization
- **uv** for package management, **Ruff** for linting/formatting
- **pytest** testing setup with coverage
- Optional PostgreSQL with async SQLAlchemy
- Docker/OrbStack support
- GitHub Actions CI/CD
- Pre-configured `.claude/` commands

#### python-react-app
Full-stack application template with:
- Python backend (FastAPI)
- React frontend (Vite + TypeScript)
- Pre-configured development environment
- `.claude/` folder with AI assistant commands

## 📝 Claude AI Integration

The `.claude/` folders contain custom commands for the Claude AI assistant:

- **analyze** - Code analysis and review commands
- **migrate** - Database and code migration helpers
- **refactor** - Code refactoring assistance
- **scaffold** - Project scaffolding commands
- **test** - Testing utilities
- **work** - General development workflow commands

These commands are automatically included when:
1. Using `chezmoi apply` in a managed project
2. Creating new projects from templates

## 🔧 Customization

### Adding New Dotfiles

1. Add the file to chezmoi management:
   ```bash
   chezmoi add ~/.config/myapp/config
   ```

2. Commit and push changes:
   ```bash
   cd $(chezmoi source-path)
   git add .
   git commit -m "Add myapp configuration"
   git push
   ```

### Creating Templates

1. Add template files to `templates/` directory
2. Use `{{variable}}` syntax for dynamic values
3. Include `.chezmoi.json.tmpl` for template variables

### Modifying Existing Files

1. Edit through chezmoi:
   ```bash
   chezmoi edit ~/.zshrc
   ```

2. Or edit directly and re-add:
   ```bash
   vim ~/.zshrc
   chezmoi add ~/.zshrc
   ```

## 🔐 Security

- No secrets or sensitive data are stored in this repository
- API keys and tokens should be managed separately
- Use environment variables or secure key management tools

## 🤝 Contributing

This is a personal dotfiles repository, but if you find something useful:

1. Fork the repository
2. Create your own version
3. Customize to your needs
4. Share your improvements!

## 📚 Resources

- [Chezmoi Documentation](https://www.chezmoi.io/)
- [Chezmoi Quick Start](https://www.chezmoi.io/quick-start/)
- [Managing Dotfiles](https://www.chezmoi.io/user-guide/manage-dotfiles/)

## 📄 License

Feel free to use any of these configurations for your own setup!

---

*Last updated: May 28, 2025*