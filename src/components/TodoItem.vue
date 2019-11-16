<template>
  <li class="field is-grouped todo-list-item" :class="{ complete: checked }">
    <input type="hidden" :value="itemId" />
    <p class="control checkbox">
      <input type="checkbox" v-model="checked" v-on:change="update" />
    </p>
    <p class="control is-expanded">
      <input class="input content"
        ref="text"
        v-on:click="showEdit"
        v-on:keyup="submit"
        v-on:blur="editItem"
        v-bind:class="[isEditing ?  '' : 'is-static']" :value="text" />
    </p>
    <p class="control">
      <button class="delete" v-on:mousedown="deleteItem" v-bind:class="[isEditing ?  '' : 'hidden']">delete</button>
    </p>
  </li>
</template>

<script>
export default {
  name: 'TodoItem',
  props: {
    itemId: String,
    content: String,
    isComplete: Boolean
  },
  data: function () {
    return {
      checked: this.isComplete,
      text: this.content,
      isEditing: false
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
    },
    showEdit: function () {
      this.isEditing = true
      this.$nextTick(() => {
        this.$refs.text.focus()
      })
    },
    submit: function (e) {
      if (e.keyCode === 13) {
        this.editItem()
        this.$refs.text.blur()
      }
    },
    editItem: function () {
      if (this.isEditing) {
        let newText = this.$refs.text.value
        this.text = newText
        var ev = {
          itemId: this.itemId,
          content: newText,
          checked: this.checked
        }
        this.$emit('update', ev)
        this.isEditing = false
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.complete .is-static {
  color: #999;
  text-decoration: line-through;
}
.hidden {
  display: none;
}
input[type=checkbox]{
  vertical-align: middle;
  height: 100%;
}
button.delete {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}
</style>
