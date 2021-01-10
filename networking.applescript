
# ----------FUNCTIONS ----------------- #



tell application "Safari" 
    -- companies = ["Facebook", "Google", "LinkedIn"]
    activate
    make new document with properties {URL:"https://www.linkedin.com/"} -- document 1
    delay 4
    tell application "System Events"
        keystroke "LinkedIn"
    end tell
    delay 3
    tell document 1
        do JavaScript "document.getElementsByClassName('search-global-typeahead__input')[0].focus();"
        -- do JavaScript "document.getElementsByClassName('search-global-typeahead__input')[0].click();"
        delay 2
        tell application "System Events"
            keystroke "Software Engineer at Facebook Sunnyvale"
            delay 0.5
            key code 36
        end tell -- end system events call
        delay 3
        do JavaScript "document.getElementById('ember1882').click();" # click the PEOPLE btn
        delay 3
        
        do JavaScript
        "
            var ents = document.getElementsByClassName('entity-result__item');  
            var looper = ents.length;
            var id = ents[0].childNodes[2].childNodes[0].id;
            var name = '';
            for(var i = 0; i < looper; i++) {
                name = ents.childNodes[1].childNodes[0].childNodes[0].childNodes[0].childNodes[0].childNodes[0].childNodes[0].childNodes[0].childNodes[0].childNodes[0].innerHTML;
                console.log(name + '\n');
            }
        "



    end tell -- endting document 1 call
end tell






# TO RUN THIS SCRIPT: SHIFT + ALT + R