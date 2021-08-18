<template>
  <transition name="modal-fade">
    <div class="modal-backdrop">
      <div class="modal"
        role="dialog"
        aria-labelledby="modalTitle"
        aria-describedby="modalDescription"
      >
        <header
          class="modal-header"
          id="modalTitle"
        >
          <slot name="header">
            Default tile!
          </slot>
          <button
            type="button"
            class="btn-close"
            @click="closeModal"
          >
            X
          </button>
        </header>

        <section
          class="modal-body"
          id="modalDescription"
        >
          <slot name="body">
            Default body!
          </slot>
        </section>

        <footer class="modal-footer">
          <button
            type="button"
            class="btn-update"
            @click="updatePortfolio"
          >
            Update!
          </button>
        </footer>
      </div>
    </div>
  </transition>
</template>

<script>
  export default {
    name: 'ModalUpdatePortfolio',
    methods: {
      closeModal() {
        this.$emit('close');
      },
      updatePortfolio() {
        this.$emit('update');
      }
    },
  };
</script>

<style>
  .modal-backdrop {
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 100;
	position: absolute;
  }

  .modal {
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    display: flex;
    flex-direction: column;
    width: 80%;
    border-radius: 10px;
  }

  .modal-header,
  .modal-footer {
    padding: 15px;
    display: flex;
  }

  .modal-header {
    position: relative;
    border-bottom: 1px solid #eeeeee;
    color: #1da1f2;
    justify-content: space-between;
  }

  .modal-footer {
    border-top: 1px solid #eeeeee;
    flex-direction: column;
  }

  .modal-body {
    position: relative;
    padding: 20px 10px;
  }

  .btn-close {
    position: absolute;
    top: 0;
    right: 0;
    border: none;
    font-size: 20px;
    padding: 10px;
    cursor: pointer;
    font-weight: bold;
    color: #1da1f2;
    background: transparent;
  }

  .btn-update {
    color: white;
    height: 40px;
    background: #1da1f2;
    border: 1px solid #1da1f2;
    border-radius: 2px;
    font-size: 20px;
    border-radius: 10px;
  }

  .modal-fade-enter,
  .modal-fade-leave-to {
    opacity: 0;
  }

  .modal-fade-enter-active,
  .modal-fade-leave-active {
    transition: opacity .5s ease;
  }
</style>