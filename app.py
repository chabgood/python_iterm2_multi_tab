#!/usr/bin/env python3.7

# brew install python3
# pip3 install iterm2
# pip3 install pyobjc


import iterm2
import AppKit

AppKit.NSWorkspace.sharedWorkspace().launchApplication_("iTerm2")

async def main(connection):
    app = await iterm2.async_get_app(connection)
    window = app.current_terminal_window
    repositories = { ‘dir’: ‘command’ }
    for repository in repositories:
        tab = await window.async_create_tab()
        await tab.async_set_title(repository)
        session = app.current_terminal_window.current_tab.current_session
        await session.async_send_text(f'cd ~/projects/{repository}\n')
        await session.async_send_text(f'{repositories[repository]}\n')
iterm2.run_until_complete(main)
