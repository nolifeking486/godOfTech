---@diagnostic disable: undefined-global
local p = plugin.register({
	name = "save-track",
	type = "hook",
	description = "Download current track with album art via yt-dlp",
	permissions = { "keymap", "exec" },
})

local OUT_DIR = "/home/devansh/Music"

p:bind("alt+g", "Download current track", function()
	local url = cliamp.track.path()
	if not url or url == "" then
		cliamp.message("Save failed: no active track", 5)
		return
	end
	if not url:match("^https?://") then
		cliamp.message("Save failed: not a streamed track", 5)
		return
	end

	local label = (cliamp.track.artist() or "Unknown") .. " - " .. (cliamp.track.title() or "Unknown")
	cliamp.message("Downloading: " .. label, 5)

	local handle, err = cliamp.exec.run("yt-dlp", {
		"-x",
		"--audio-format",
		"opus",
		"--audio-quality",
		"0",
		"--embed-thumbnail",
		"--embed-metadata",
		"--convert-thumbnails",
		"jpg",
		"--no-playlist",
		"-o",
		OUT_DIR .. "/%(artist,uploader)s - %(title)s.%(ext)s",
		"--",
		url,
	}, {
		timeout = 600,
		on_stderr = function(line)
			cliamp.log.info("yt-dlp: " .. tostring(line))
		end,
		on_exit = function(code)
			if code == 0 then
				cliamp.message("Saved: " .. label, 8)
			else
				cliamp.message("Download failed (exit " .. tostring(code) .. "), see plugins.log", 8)
			end
		end,
	})

	if not handle then
		cliamp.message("Could not start yt-dlp: " .. tostring(err), 8)
	end
end)
