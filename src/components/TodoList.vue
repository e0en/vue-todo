<template>
<div class="todo-list">
  <h1>{{ msg }}</h1>
  <ul>
  </ul>
</div>
</template>

<script>
export default {
  name: 'TodoList',
  props: {
    msg: String
  }
}
</script>

<style scoped lang="less">
</style>
