// 很多文本编辑器都可以设置为保存文件时自动执行gofmt，所以你的源代码应该总是会被格式化。这里还有一个相关的工具，goimports，
// 会自动地添加你代码里需要用到的import声明以及需要移除的import声明。这个工具并没有包含在标准的分发包中，然而你可以自行安装：
// $ go get golang.org/x/tools/cmd/goimports

package main

import (
	"fmt"
)

func main() {
	fmt.Println("你好，golang！")
}
