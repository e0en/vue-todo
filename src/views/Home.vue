<template>
  <div class="todo_list">
    <TodoList name="Todo" :items="items" />
  </div>
</template>

<script>
// @ is an alias to /src
import TodoList from '@/components/TodoList.vue'

export default {
  name: 'home',
  components: {
    TodoList
  },
  data: function () {
    return {
      items: [
        { itemId: '0', content: 'Buy milk', isComplete: false },
        { itemId: '1', content: 'Buy eggs', isComplete: true }
      ]
    }
  }
}
</script>
