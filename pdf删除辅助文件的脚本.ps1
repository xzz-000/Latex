# 删除 LaTeX 辅助文件的脚本（兼容中文和特殊字符）
# 强制 UTF-8 编码
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8
# 1. 定义要删除的文件扩展名列表
$extensions = @(
    "*.aux",
    "*.log",
    "*.toc",
    "*.out",
    "*.synctex.gz",
    "*.synctex(busy)",  # 匹配类似 "电饭煲.synctex(busy)" 的文件
    "*.hd",
    "*.bbl",
    "*.lot"
)

# 2. 遍历所有扩展名并删除匹配的文件
foreach ($ext in $extensions) {
    # 使用 Get-ChildItem -Filter 而不是 -Include，因为它更可靠且支持特殊字符
    Get-ChildItem -Path . -Filter $ext -File -ErrorAction SilentlyContinue | ForEach-Object {
        try {
            # 尝试删除文件，-Force 用于删除只读或隐藏文件
            Remove-Item $_.FullName -Force -ErrorAction Stop
            Write-Host "已删除: $($_.FullName)" -ForegroundColor Green
        }
        catch {
            Write-Host "无法删除: $($_.FullName) (可能被占用)" -ForegroundColor Yellow
        }
    }
}

# Write-Host "清理完成！" -ForegroundColor Cyan