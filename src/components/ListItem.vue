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
    itemId: String,
    content: String,
    checked: Boolean
  }
}
</script>

<style scoped lang="less">
.complete {
  color: #999;
  text-decoration: line-through;
}
input[type=checkbox] {
  margin-right: 1em;
}
</style>
