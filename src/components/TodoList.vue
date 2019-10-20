<template>
<div class="todo-list">
  <h1>{{ name }}</h1>
  <form>
    <label for="newItem">Add new task</label><br />
    <input type="text" name="newItem" />
  </form>
  <ul>
    <ListItem v-for="i in items" :key="i.itemId"
      :itemId="i.itemId" :content="i.content" :isComplete="i.isComplete"
      v-on:update="update"
    />
  </ul>
</div>
</template>

<script>
// @ is an alias to /src
import ListItem from '@/components/ListItem.vue'

export default {
  name: 'TodoList',
  props: {
    name: String
  },
  data: function () {
    return {
      items: [
        { itemId: '0', content: 'Buy milk', isComplete: false },
        { itemId: '1', content: 'Buy eggs', isComplete: true }
      ]
    }
  },
  components: {
    ListItem
  },
  methods: {
    update: function (ev) {
      console.log(ev)
      this.items.forEach(function (item) {
        if (item.itemId === ev.itemId) {
          item.isComplete = ev.checked
        }
      })
    }
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
