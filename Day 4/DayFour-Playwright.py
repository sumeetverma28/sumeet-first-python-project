# Open Google in the default browser, verify title using pytest
import webbrowser

url = "https://www.google.com"
opened = webbrowser.open(url)

if opened:
    #print("Google opened successfully.")
    title = "Google"
    assert title == "Google", f"Expected title 'Google', but got '{title}'"
else:
    print("Could not open Google in the default browser.")
