#!/bin/bash

# Create Dev directory structure if it doesn't exist
mkdir -p ~/Dev/QoE_App

# Create symlink to MCP config if QoE_App directory exists and symlink doesn't exist
if [ -d ~/Dev/QoE_App ] && [ ! -e ~/Dev/QoE_App/.mcp.json ]; then
    ln -s ~/.mcp.json ~/Dev/QoE_App/.mcp.json
    echo "Created symlink: ~/Dev/QoE_App/.mcp.json -> ~/.mcp.json"
fi
