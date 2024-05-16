# Define the name of the output zip file
ZIPFILE = Clothoids.zip

# Define the directories and files to exclude
EXCLUDE_PATTERNS = \
	"*.git*" \
	"**/*.git*" \
	"doc*" \
	"**/doc*" \
	"__MACOSX*" \
	"*.pdf" \
	"*.jpeg" \
	"*.jpg" \
	"*.png" \
	"*.gif" \
	"*.bmp" \
	"*.tiff" \
	"*.svg" \
	"Clothoids*" \
	"build*" \
	"maple*" \
	"standalone_project*" \
	"Xcode*" \
	"toolbox*" \
	"submodules/Utils/ThirdParties/Eigen/eigen*" \
	"submodules/Utils/ThirdParties/fmt/fmt*"

EXCLUDES = $(foreach pattern,$(EXCLUDE_PATTERNS),-x $(pattern))

# Define the directories and files to include
INCLUDES = *

# The target to create the zip file
$(ZIPFILE):
	@echo "Removing existing $(ZIPFILE)..."
	@rm -f $(ZIPFILE)
	@echo "Creating $(ZIPFILE)..."
	@zip -r $(ZIPFILE) $(INCLUDES) $(EXCLUDES)
	@echo "$(ZIPFILE) created successfully."

# A clean target to remove the generated zip file
clean: 
	@echo "Cleaning up..."
	@rm -f $(ZIPFILE) 
	@echo "Clean up completed."

release_zip: clean $(ZIPFILE)

