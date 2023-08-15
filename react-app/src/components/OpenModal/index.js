import React from 'react';
import { useModal } from '../../context/Modal';

function OpenModal({
  modalComponent, // component to render inside the modal
  buttonText, // text of the button that opens the modal
  isOpen,
  onButtonClick, // optional: callback function that will be called once the button that opens the modal is clicked
  onModalClose // optional: callback function that will be called once the modal is closed
}) {
  const { setModalContent, setOnModalClose } = useModal();

  if (onModalClose) setOnModalClose(onModalClose);
  setModalContent(modalComponent);
  if (isOpen) onButtonClick();

  return (
    <></>
  );
}

export default OpenModal;