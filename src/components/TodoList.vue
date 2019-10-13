<template>
<div class="todo-list">
  <h1>{{ msg }}</h1>
  <ul>
    <ListItem v-for="i in 10" :key="i" :content="i"/>
  </ul>
</div>
</template>

<script>
// @ is an alias to /src
import ListItem from '@/components/ListItem.vue'

export default {
  name: 'TodoList',
  props: {
    msg: String
  },
  components: {
    ListItem
  }
}
</script>

<style scoped lang="less">
</style>
