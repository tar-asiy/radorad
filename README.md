# Radorad - Interactive Wheel Dictionary Builder

## What is Radorad?

Radorad is an interactive tool for creating and managing hierarchical dictionaries visualized as colorful wheels. Perfect for language learning or any structured vocabulary organization.

### Key Features
- 🎨 Visual wheel-based representation
- 🌍 Supports English, German, and Ukrainian
- 📚 Three-level hierarchy system
- 💾 Save/load dictionaries as JSON
- 🎮 Interactive command-line interface

### What Can You Do With It?
- Create structured vocabulary collections
- Build hierarchical concept maps
- Visualize relationships between terms
- Manage multi-level classifications

I'll add those sections to the [[README]]:

## Technical Details & Getting Started

### Installation Requirements

#### Windows
1. **Install Python**
   - Download from [python.org](https://python.org)
   - Run installer, check "Add Python to PATH"
   - Verify installation: `python --version` in Command Prompt

2. **Install Required Packages**
   ```bash
   pip install matplotlib tkinter
   ```

#### macOS
1. **Install/Update Python**
   ```bash
   # Using Homebrew
   brew install python
   # Verify installation
   python3 --version
   ```

2. **Install Required Packages**
   ```bash
   pip3 install matplotlib tkinter
   ```

#### Linux
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip python3-tk
pip3 install matplotlib

# Fedora
sudo dnf install python3 python3-pip python3-tkinter
pip3 install matplotlib
```

### Running Radorad

1. **Download**
   - Get `radorad.py` from the repository
   - Place it in your preferred directory

2. **Make Executable** (macOS/Linux only)
   ```bash
   chmod +x radorad.py
   ```

3. **Run the Program**
   ```bash
   # Windows
   python radorad.py

   # macOS/Linux
   ./radorad.py
   # or
   python3 radorad.py
   ```

### Common Issues & Solutions

#### Program Won't Start
- Check Python installation: `python --version`
- Verify packages: `pip list | grep matplotlib`
- Try reinstalling packages

#### No GUI Window
- Check Tkinter: `python -m tkinter`
- Reinstall Tkinter if needed

#### Can't Save Dictionary
- Check write permissions in directory
- Ensure valid file name
- Try different save location

### Command Reference

When running Radorad, you'll use these commands:

#### Root Level Commands
- `a` - Add new category
- `go X` - Navigate to item X
- `view N` - Change view depth (1-3)
- `done` - Save and exit

#### Item Level Commands
- `r` - Rename current item
- `a` - Add sub-item
- `d` - Delete current item
- `done` - Return to root
- `go X` - Navigate to item X

### Default File Structure
```
your-directory/
├── radorad.py      # Main program
├── dict/           # Recommended folder for json-dictationaries
│   ├── dict1.json
│   └── dict2.json
└── img/            # Recommended folder for generated wheels
    └── wheel1.png
    └── wheel2.pdf
```

### Dictionary File Format
```json
{
  "rings": [
    [
      {
        "word": "Category1",
        "color": "#FFD300",
        "sub": [
          {
            "word": "SubCategory1",
            "sub": [
              {
                "word": "Detail1"
              }
            ]
          }
        ]
      }
    ]
  ]
}
```

### Development Notes
- Python 3.6+ required
- Uses matplotlib for visualization
- Tkinter for file dialogs
- JSON for data storage
- UTF-8 encoding for multilingual support

### Customization
- Edit color schemes in `BASE_COLORS`
- Modify wheel dimensions in `build_and_show_wheel()`
- Adjust text sizes in `draw_nested()`

### Getting Help
- Check command line prompts
- Use `--help` flag for options
- Refer to this documentation
- Check issue tracker on repository
## Creating Your Wheel Dictionary: A User Guide

### Understanding the Wheel Structure

Think of your dictionary as a colorful wheel with three rings:
1. **Outer Ring**: Main categories (like "Personality", "Magic", "Skills")
2. **Middle Ring**: Basic terms (common descriptors)
3. **Inner Ring**: Detailed terms (specific descriptors)

### Tips for Building Your Dictionary

#### 1. Planning Your Categories
- Start with broad themes (outer ring)
- Choose clear, distinct categories
- Use colors to differentiate main themes
- Keep category names simple and clear

#### 2. Adding Basic Terms (Middle Ring)
- Use everyday vocabulary
- Choose commonly used descriptors
- Keep terms straightforward
- Think about practical usage
- Aim for 3-7 terms per category

#### 3. Adding Detailed Terms (Inner Ring)
- Add specific variations
- Include nuanced descriptions
- Connect to parent terms
- Limit to 2-5 details per basic term

#### 4. Best Practices
- **Keep It Balanced**: Similar number of terms in each category
- **Stay Focused**: Each term should clearly relate to its parent
- **Be Consistent**: Maintain similar detail level within each ring
- **Think Practical**: Every term should be useful in your context

### Example: Character Traits Wheel

```
Outer Ring: "Personality"
├── Middle Ring: "Friendly"
│   ├── Inner Ring: "Outgoing"
│   ├── Inner Ring: "Welcoming"
│   └── Inner Ring: "Sociable"
└── Middle Ring: "Careful"
    ├── Inner Ring: "Meticulous"
    └── Inner Ring: "Thorough"
```
### Quick Tips
- Start small, expand gradually
- Test terms in context
- Review and refine regularly
- Keep your audience in mind
- Use clear, unambiguous terms
