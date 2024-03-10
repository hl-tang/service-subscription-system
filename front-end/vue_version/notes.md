vite pnpm创建项目



## 删掉没用的东西

`src/components`下的`HelloWorld.vue` 删掉

`App.vue`里面东西删光

`style.css`里面东西删光



## 配置router

导入`vue-router`

```
pnpm add vue-router@4
```



`App.vue`写入

```vue
<template>
  <router-view />
</template>
```



src/下建个pages目录放page(以前的习惯叫views)

src/下建个router目录，下面创建index.js定义路由

pages下创个Play.vue，配好router，随便在里面尝试 (最后.gitignore里加上`/src/pages/Play.vue`)



参考以前做的项目，修改main.js (导入vue-router)，将路由应用到跟实例上



## Tailwind CSS

参考 https://tailwindcss.com/docs/guides/vite#vue

```
pnpm add -D tailwindcss postcss autoprefixer
```



## Vuetify

```
pnpm i vuetify
```

