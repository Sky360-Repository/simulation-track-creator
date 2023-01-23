FROM sky360/sky360lib:1.0.2

# ** [Optional] Uncomment this section to install additional packages. **
#
# ENV DEBIAN_FRONTEND=noninteractive
# RUN apt-get update \
#    && apt-get -y install --no-install-recommends <your-package-list-here> \
#    #
#    # Clean up
#    && apt-get autoremove -y \
#    && apt-get clean -y \
#    && rm -rf /var/lib/apt/lists/*
# ENV DEBIAN_FRONTEND=dialog

RUN apt-get update && apt-get -y install xvfb xclip

RUN pip install dynaconf pyperclip

# Set up auto-source of workspace for ros user
ARG WORKSPACE
