import settings

login = '{"op":2,"d":{"token":"'+settings.token+'","capabilities":30717,"properties":{"os":"Linux","browser":"Firefox","device":"","system_locale":"en-US","browser_user_agent":"Mozilla/5.0 (X11; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0","browser_version":"126.0","os_version":"","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":298544,"client_event_source":null,"design_id":0},"presence":{"status":"unknown","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_versions":{}}}}'
guild = '{"op":37,"d":{"subscriptions":{"'+settings.guild+'":{"typing":true,"threads":true,"activities":true,"members":[],"member_updates":false,"channels":{},"thread_member_lists":[]}}}}'
ping = '{"op":1, "d":12}'
