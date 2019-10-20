<template>
  <li class="todo-list-item" :class="{ complete: checked }">
    <input type="checkbox" v-model="checked" v-on:change="updateIsComplete" />
    <input type="hidden" :value="itemId" />
    <span class="content">{{ content }}</span>
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
    updateIsComplete: function () {
      var ev = {
        itemId: this.itemId,
        checked: this.checked
      }
      this.$emit('updated', ev)
      console.log(this.content + ', ' + this.checked.toString() + ', ' + this.itemId)
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
