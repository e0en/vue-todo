<template>
  <li class="todo-list-item">
    <input type="checkbox" />
    <span class="content">{{ content }}</span>
  </li>
</template>

<script>
export default {
  name: 'ListItem',
  props: {
    content: String,
    checked: Boolean
  }
}
</script>

<style scoped lang="less">
</style>
