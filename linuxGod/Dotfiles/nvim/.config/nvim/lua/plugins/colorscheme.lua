return {
  { "nyoom-engineering/oxocarbon.nvim" },
  {
    "LazyVim/LazyVim",
    opts = {
      colorscheme = function()
        vim.cmd.colorscheme("oxocarbon")

        -- Clear background for primary UI elements
        local hl_groups = {
          "Normal",
          "NormalNC",
          "NormalFloat",
          "FloatBorder",
          "SignColumn",
          "StatusLine",
          "StatusLineNC",
          "EndOfBuffer",
        }

        for _, group in ipairs(hl_groups) do
          vim.api.nvim_set_hl(0, group, { bg = "none", ctermbg = "none" })
        end
      end,
    },
  },
}
