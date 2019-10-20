<template>
<div class="todo-list">
  <h1>{{ name }}</h1>
  <form>
    <label for="newItem">Add new task</label><br />
    <input type="text" name="newItem" />
  </form>
  <ul>
    <ListItem v-for="i in items" :key="i.itemId" :itemId="i.itemId" :content="i.content" :isComplete="i.isComplete"/>
  </ul>
</div>
</template>

<script>
// @ is an alias to /src
import ListItem from '@/components/ListItem.vue'

export default {
  name: 'TodoList',
  props: {
    name: String,
    items: Array
  },
  components: {
    ListItem
  }
}
</script>

<style scoped lang="less">
div.todo-list {
  margin: 0 auto;
  max-width: 900px;
  text-align: left;
}
ul {
  list-style-type: none;
  line-height: 2em;
  margin-left: 0;
  padding-left: 0;
}
</style>
