/**
 * js/modules/drag-drop.js
 * Generic drag-and-drop reordering for list rows.
 * Used by Orders (tech allocation rows) and Daily (supply log rows).
 *
 * Usage:
 *   CCS.DragDrop.init('.tech-alloc-row', onReorder)
 *   // onReorder(newOrderedArray) called after drop
 */

'use strict';

(function () {
  let _dragging = null;
  let _onReorder = null;

  function _getItems(container) {
    return [...container.children].filter(el => el.matches('[data-draggable]'));
  }

  function init(selector, onReorder) {
    _onReorder = onReorder;

    document.querySelectorAll(selector).forEach(row => {
      row.setAttribute('draggable', 'true');
      row.dataset.draggable = '1';

      row.addEventListener('dragstart', e => {
        _dragging = row;
        row.style.opacity = '0.4';
        e.dataTransfer.effectAllowed = 'move';
      });

      row.addEventListener('dragend', () => {
        row.style.opacity = '';
        document.querySelectorAll('[data-draggable]').forEach(r => r.classList.remove('drag-over'));
        _dragging = null;
      });

      row.addEventListener('dragover', e => {
        e.preventDefault();
        e.dataTransfer.dropEffect = 'move';
        if (row !== _dragging) {
          document.querySelectorAll('[data-draggable]').forEach(r => r.classList.remove('drag-over'));
          row.classList.add('drag-over');
        }
      });

      row.addEventListener('drop', e => {
        e.preventDefault();
        if (!_dragging || _dragging === row) return;

        const container = row.parentNode;
        const items = _getItems(container);
        const fromIdx = items.indexOf(_dragging);
        const toIdx   = items.indexOf(row);
        if (fromIdx < 0 || toIdx < 0) return;

        // DOM reorder
        if (fromIdx < toIdx) container.insertBefore(_dragging, row.nextSibling);
        else                  container.insertBefore(_dragging, row);

        row.classList.remove('drag-over');

        // Notify caller with new order of data-keys
        const newOrder = _getItems(container).map(el => el.dataset.key);
        _onReorder?.(newOrder);
      });
    });
  }

  /** Apply ordering to an array given an array of keys, matching item[keyField] */
  function applyOrder(arr, orderedKeys, keyField = 'id') {
    const map = new Map(arr.map(item => [item[keyField], item]));
    return orderedKeys.map(k => map.get(k)).filter(Boolean);
  }

  CCS.DragDrop = { init, applyOrder };
})();
