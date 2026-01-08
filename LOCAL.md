# Running Locally

This guide will help you run this Jekyll website on your local machine.

## Prerequisites

- Ruby (2.7 or higher recommended)
- Bundler gem

## Installation Steps

### 1. Check Ruby Installation

```bash
ruby --version
```

If Ruby is not installed, install it using one of these methods:

**macOS (using Homebrew):**
```bash
brew install ruby
```

**Or use rbenv (recommended for managing Ruby versions):**
```bash
brew install rbenv ruby-build
rbenv install 3.1.0
rbenv global 3.1.0
```

### 2. Install Bundler

```bash
gem install bundler
```

**Note:** If you get permission errors, try:
```bash
gem install bundler --user-install
```

Or add `--user-install` to your gem configuration:
```bash
bundle config set --local path 'vendor/bundle'
```

### 3. Install Project Dependencies

Navigate to the project directory and install dependencies:

```bash
cd /Users/ttpho/Documents/GitHub/ttpho.github.io
bundle install
```

### 4. Run the Local Server

Start the Jekyll development server:

```bash
bundle exec jekyll serve
```

Your website will be available at: **http://localhost:4000**

## Useful Commands

### Run with Live Reload
Automatically refresh the browser when files change:
```bash
bundle exec jekyll serve --livereload
```

### Include Draft Posts
Show posts in the `_drafts` folder:
```bash
bundle exec jekyll serve --drafts
```

### Use Different Port
Run on a different port (e.g., 4001):
```bash
bundle exec jekyll serve --port 4001
```

### Build Without Serving
Just build the site without starting a server:
```bash
bundle exec jekyll build
```

## Troubleshooting

### Permission Errors with Gems
If you encounter permission errors when installing gems, avoid using `sudo`. Instead:

1. Configure bundler to install gems locally:
```bash
bundle config set --local path 'vendor/bundle'
bundle install
```

2. Or install gems to user directory:
```bash
gem install bundler --user-install
```

### Port Already in Use
If port 4000 is already in use:
```bash
bundle exec jekyll serve --port 4001
```

### Dependencies Issues
If you encounter dependency conflicts:
```bash
bundle update
bundle install
```

### Ruby Version Issues
If the project requires a specific Ruby version, consider using rbenv:
```bash
rbenv install 3.1.0
rbenv local 3.1.0
bundle install
```

## File Structure

- `_config.yml` - Main configuration file
- `_posts/` - Blog posts (format: YYYY-MM-DD-title.md)
- `_layouts/` - Page layouts
- `_includes/` - Reusable components
- `assets/` - CSS, JavaScript, images
- `_site/` - Generated site (created after build, ignored by git)

## Making Changes

1. Edit markdown files or add new posts to `_posts/`
2. Save your changes
3. Jekyll will automatically rebuild (if using `--livereload`)
4. Refresh your browser to see changes

## Stop the Server

Press `Ctrl + C` in the terminal where Jekyll is running.
