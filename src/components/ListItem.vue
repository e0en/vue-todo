<template>
  <li class="todo-list-item" :class="{ complete: checked }">
    <input type="checkbox" v-model="checked" v-on:change="update" />
    <input type="hidden" :value="itemId" />
    <span class="content">{{ content }}</span>
    <button class="delete" v-on:click="deleteItem">delete</button>
  </li>
</template>

<script>
export default {
  name: 'ListItem',
  props: {
    itemId: String,
    content: String,
    isComplete: Boolean
  },
  data: function () {
    return {
      checked: this.isComplete
    }
  },
  methods: {
    update: function () {
      var ev = {
        itemId: this.itemId,
        content: this.content,
        checked: this.checked
      }
      this.$emit('update', ev)
    },
    deleteItem: function () {
      this.$emit('deleteItem', this.itemId)
    }
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
